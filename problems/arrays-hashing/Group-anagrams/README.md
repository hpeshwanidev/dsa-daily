# 🗂️ Group Anagrams — LeetCode #49

🔗 **[View Problem](https://leetcode.com/problems/group-anagrams/)**  
💡 **Difficulty:** Medium  

---

## 🧠 Approach

- Maintain a `visited[]` array to track which strings have already been grouped.
- For each string:
  - If it is not visited, start a new group.
  - Compare it with every following string to check if they are anagrams.
  - If two strings are anagrams, add the second one to the same group and mark it visited.
- Use a helper function `isAnagram()` that:
  - Builds two frequency hash maps for both strings.
  - Returns true if the maps are identical.
- Add each completed group to the final answer.

---

## ⏱️ Complexity Analysis

| Complexity | Description |
|-----------|-------------|
| **Time**  | O(n² × k) — comparing each pair, `k` = average string length |
| **Space** | O(k) per comparison, for two hashmap frequency tables |

---