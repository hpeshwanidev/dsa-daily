# 🧵 Longest Common Prefix — LeetCode #14

🔗 **[View Problem](https://leetcode.com/problems/longest-common-prefix/)**  
💡 **Difficulty:** Easy  

---

## 🧠 Approach

- First, compute the length of the shortest string in the array — since the prefix cannot be longer than that.
- If there is only one string, return it directly.
- For exactly 3 strings, compare characters at each index across all 3 and append matching characters to the result.
- For more than 3 strings:
  - Compare characters at each index `j` across three consecutive strings (`i-1`, `i`, `i+1`).
  - If all match at the same index, append to the result.
- Return the built prefix string.

---

## ⏱️ Complexity Analysis

| Complexity | Description |
|-----------|-------------|
| **Time**  | O(n × m) — `n` strings, `m` = length of shortest string |
| **Space** | O(m) — storing the prefix result |
