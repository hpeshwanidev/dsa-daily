# 🧩 Concatenation of Array — LeetCode #1929

🔗 **[View Problem](https://leetcode.com/problems/concatenation-of-array/)**  
💡 **Difficulty:** Easy  

---

## 🧠 Approach

- Create a new array `result` of size `2 * n`, where `n` is the length of `nums`.  
- Loop through the array and assign values:  
  - `result[i] = nums[i]`  
  - `result[i + n] = nums[i]`  
- This effectively appends the array to itself, forming the concatenation.

---

## ⏱️ Complexity Analysis

| Complexity | Description |
|-------------|-------------|
| **Time** | O(n) — iterate once through the array |
| **Space** | O(2n) → O(n) — new array of double size |

---