class Solution {
    public String longestCommonPrefix(String[] strs) {
        String sol = "";
        int l = strs[0].length();
        for(int i=1; i<strs.length; i++){
            if (l > strs[i].length()){
                l = strs[i].length();
            }
        }
        if(strs.length==3){
            for(int j=0; j<l; j++){
                if(strs[0].charAt(j) == strs[1].charAt(j) && strs[1].charAt(j) == strs[2].charAt(j)){
                    sol+=strs[1].charAt(j);
                }
            }
        }
        else if (strs.length==1){
            sol+=strs[0];
        }
        for (int i =1; i<strs.length-2; i++){
            for(int j=0; j<l; j++){
                if(strs[i-1].charAt(j) == strs[i].charAt(j) && strs[i].charAt(j) == strs[i+1].charAt(j)){
                    sol+=strs[i-1].charAt(j);
                }
            }
        }
        return sol ; 
    }
}
