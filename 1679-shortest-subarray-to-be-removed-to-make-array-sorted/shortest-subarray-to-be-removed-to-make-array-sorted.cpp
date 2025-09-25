class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int n = arr.size();
        int left = 0;
        int right = n-1;
        int midSize = 0;
        int leftSize = 1;
        int rightSize = 1;

        while(left < n-1){
            if(arr[left] <= arr[left + 1]){
                left = left + 1;
                leftSize += 1;
            } else {
                break;
            }
        }

        while(right > 0){
            if(arr[right] >= arr[right - 1]){
                right = right - 1;
                rightSize += 1;
            } else {
                break;
            }
        }
        
        cout<<"right "<<right<<endl;

        int rightTwo = n-1;

        while(left >= 0 && rightTwo >= right){
            cout<<" rightTwo "<<rightTwo<<" left "<<left<<endl;
            if(arr[rightTwo] >= arr[left]){
                midSize = max(midSize, (left + 1) + (n - rightTwo));
                rightTwo -= 1;
            } else{
                left -= 1;
            }
        }

        int maxAns = max(rightSize, max(leftSize, midSize));
        cout<<"righSize "<<rightSize<<" leftSize "<<leftSize<<" midSize "<<midSize<<endl;
        return max(n - maxAns, 0);
    }
};