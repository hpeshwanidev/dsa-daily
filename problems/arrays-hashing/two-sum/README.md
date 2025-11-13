# 🎯 Two Sum — LeetCode #1

🔗 **[View Problem](https://leetcode.com/problems/two-sum/)**  
💡 **Difficulty:** Easy  

---

## 🧠 Approach

- Use a brute-force approach with two nested loops.  
- For each element, check if there exists another element such that their sum equals the target.  
- If found, return their indices as an integer array.  
- If no such pair exists, return `[-1, -1]`.

---

## ⏱️ Complexity Analysis

| Complexity | Description |
|-------------|-------------|
| **Time** | O(n²) — two nested loops compare each pair |
| **Space** | O(1) — no additional data structures used |

---