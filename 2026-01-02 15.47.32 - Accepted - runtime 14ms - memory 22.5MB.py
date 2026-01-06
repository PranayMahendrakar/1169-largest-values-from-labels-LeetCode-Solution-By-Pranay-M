class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # Pair values with labels and sort by value descending
        items = sorted(zip(values, labels), reverse=True)
        
        label_count = {}
        result = 0
        count = 0
        
        for value, label in items:
            if count >= numWanted:
                break
            
            # Check if we can use this label
            if label_count.get(label, 0) < useLimit:
                result += value
                label_count[label] = label_count.get(label, 0) + 1
                count += 1
        
        return result