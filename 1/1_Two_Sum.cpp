#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int complement;
        vector <int> result;
        for(int i = 0; i < nums.size(); i++){
            complement = target - nums[i];
            for (int j = i+1; j < nums.size(); j++){
                if(nums[j] == complement){
                    result.push_back(i);
                    result.push_back(j);
                    break;
                }
                
            }
        }
        return result;
    }
};