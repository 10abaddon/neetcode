
class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> db = new HashSet<>();
        for(int i=0;i<nums.length;i++){
            if(db.contains(nums[i]))
            return true;
            db.add(nums[i]);
        }
        return false;

      
    }
}
