# 🔤 Valid Anagram — LeetCode #242

🔗 **[View Problem](https://leetcode.com/problems/valid-anagram/)**  
💡 **Difficulty:** Easy  

---

## 🧠 Approach

- If the two strings have different lengths, return `false` immediately.  
- Create two hash maps (`a` and `b`) to count character frequencies in both strings.  
- Traverse each string:  
  - Increment the count for each character in its respective map.  
- Finally, compare both maps using `.equals()` — if they are identical, the strings are anagrams.

---

## ⏱️ Complexity Analysis

| Complexity | Description |
|-------------|-------------|
| **Time** | O(n) — single pass through both strings |
| **Space** | O(1) or O(k) — where *k* is the number of unique characters |

---