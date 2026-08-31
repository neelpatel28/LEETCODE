class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        first = -1
        previous = -1
        min_distance = float("inf")
        position = 1

        prev = head
        curr = head.next

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):

                if previous != -1:
                    min_distance = min(min_distance, position - previous)

                if first == -1:
                    first = position

                previous = position

            prev = curr
            curr = curr.next
            position += 1

        if first == -1 or first == previous:
            return [-1, -1]

        return [min_distance, previous - first]
