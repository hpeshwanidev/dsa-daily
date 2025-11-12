import java.util.*;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> a = new HashMap<>();
        Map<Character, Integer> b = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (a.containsKey(c)) a.put(c, a.get(c) + 1);
            else a.put(c, 1);
        }

        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            if (b.containsKey(c)) b.put(c, b.get(c) + 1);
            else b.put(c, 1);
        }

        return a.equals(b);
    }
}