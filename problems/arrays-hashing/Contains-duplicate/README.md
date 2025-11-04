# 🔁 Contains Duplicate — LeetCode #217

🔗 **[View Problem](https://leetcode.com/problems/contains-duplicate/)**  
💡 **Difficulty:** Easy  

---

## 🧠 Approach

- If the array has only one element, return `false` — since no duplicates are possible.  
- Use two nested loops:  
  - Compare each element with every other element after it.  
  - If any two elements are equal, return `true`.  
- If no duplicates are found after all comparisons, return `false`.

---

## ⏱️ Complexity Analysis

| Complexity | Description |
|-------------|-------------|
| **Time** | O(n²) — nested loops compare every pair |
| **Space** | O(1) — no extra data structures used |

---

