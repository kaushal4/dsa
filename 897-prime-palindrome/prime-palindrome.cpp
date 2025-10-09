class Solution {
public:
    bool isPrime(int num){
        if(num == 2) return true;
        for(int i = 2; i <= sqrt(num); i++){
            if(num%i == 0) return false;
        }
        return true;
    }

    int primePalindrome(int n) {
        if(n <= 9){
            for(int i = 2; i <= 9; i++){
                if(i >= n && isPrime(i)) return i;
            }
        }
        if(n <= 11) return 11;
        if(n <= 999){
            for(int i = 10; i <= 99; i++){
                string num_str = to_string(i);
                string first_half = num_str.substr(0, 1);
                reverse(first_half.begin(), first_half.end());
                string new_num_str = num_str + first_half;
                int new_num = stoi(new_num_str);
                if(new_num >= n && isPrime(new_num)) return new_num;
            }
        }
        if(n <= 99999){
            for(int i = 100; i <= 999; i++){
                string num_str = to_string(i);
                string first_half = num_str.substr(0, 2);
                reverse(first_half.begin(), first_half.end());
                string new_num_str = num_str + first_half;
                int new_num = stoi(new_num_str);
                if(new_num >= n && isPrime(new_num)) return new_num;
            }
        }
        if(n <= 9999999){
            for(int i = 1000; i <= 9999; i++){
                string num_str = to_string(i);
                string first_half = num_str.substr(0, 3);
                reverse(first_half.begin(), first_half.end());
                string new_num_str = num_str + first_half;
                int new_num = stoi(new_num_str);
                if(new_num >= n && isPrime(new_num)) return new_num;
            }
        }
        if(n <= 199999991){
            for(int i = 10000; i <= 19999; i++){
                string num_str = to_string(i);
                string first_half = num_str.substr(0, 4);
                reverse(first_half.begin(), first_half.end());
                string new_num_str = num_str + first_half;
                int new_num = stoi(new_num_str);
                if(new_num >= n && isPrime(new_num)) return new_num;
            }
        }
        return -1;
    }
};