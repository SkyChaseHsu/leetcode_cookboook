/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

 var threeSumClosest = function(nums, target) {
    let len = nums.length;
    let best = Math.pow(10, 7);
    nums.sort((a,b) => a - b);
    for (let i = 0; i < len; i++) {
        if (i > 0 && nums[i] == nums[i-1])
            continue;
        let left = i + 1;
        let right = len - 1;
        while (left < right) {
            let sum = nums[i] + nums[left] + nums[right];

            best = Math.abs(sum - target) < Math.abs(best - target) ? sum: best;
            if (sum == target) {
                return target;
            } else if (sum < target) {
                while (left < right && nums[left] == nums[left+1])
                    left++;
                left++;
            } else {
                while (left < right && nums[right] == nums[right-1])
                    right--;
                right--;
            }
        }
    }

    return best;
};