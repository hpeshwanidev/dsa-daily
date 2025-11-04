class Solution {
    public boolean containsDuplicate(int[] nums) { 
        if(nums.length == 1){
            return false;
        }
            for(int a=0; a<nums.length-1; a++){
                for(int b=a+1; b<nums.length;b++){
                    if(nums[a] == nums[b]){
                        return true;
                    }
                }          
            }
            return false;
        
    }
    }
