class Solution:

  def countDaysTogether(
      self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
  ) -> int:
    # Days in each month for a non-leap year
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Helper function to convert "MM-DD" string to day number of the year
    def date_to_day_of_year(date_str: str) -> int:
      month = int(date_str[:2])
      day = int(date_str[3:])
      return sum(days_in_months[: month - 1]) + day

    # Convert all arrival and departure dates into absolute day integers
    alice_start = date_to_day_of_year(arriveAlice)
    alice_end = date_to_day_of_year(leaveAlice)
    bob_start = date_to_day_of_year(arriveBob)
    bob_end = date_to_day_of_year(leaveBob)

    # Find the bounds of the overlapping window
    overlap_start = max(alice_start, bob_start)
    overlap_end = min(alice_end, bob_end)

    # Calculate total days; return 0 if they don't overlap
    return max(0, overlap_end - overlap_start + 1)
