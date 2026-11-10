class Solution {
    public int[] twoSum(int[] nums, int target) {
        int temp;
        for(int i=0;i<nums.length-1;i++){
            for(int j=i+1;j<nums.length;j++){
             temp=nums[i]+nums[j];
            if(temp==target){
               return new int[] {i,j};
            }}
        }
        throw new IllegalArgumentException("no match found");
         
    }
}
