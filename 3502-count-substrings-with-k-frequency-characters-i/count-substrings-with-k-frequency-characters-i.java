class Solution {
    public int numberOfSubstrings(String s, int k) {
        int n = s.length();
        int totalSubstrings = (((n+1)*n)/2);

        if(k==1)
        return totalSubstrings;

        int left = 0;
        int right = 0;
        int count = 1;

        HashMap<Character,Integer> mp = new HashMap<>();
        if (s.length() == 0){
            return 0;
        }
        mp.put(s.charAt(0), mp.getOrDefault(s.charAt(0), 0) + 1);

        int maxFreq = 1;

        while(right < n-1)
        {
            char c = s.charAt(right + 1);
            maxFreq = 0;
            if(mp.containsKey(c))
            {
               maxFreq = Math.max(maxFreq, mp.get(c));
            }

            if(maxFreq<k-1)
            {
                right++;
                char rightChar = s.charAt(right);
                mp.put(rightChar, mp.getOrDefault(rightChar, 0) + 1);
                count+= (right - left + 1);
            }
            else
            {
                char leftc = s.charAt(left);
                mp.put(leftc, mp.get(leftc) - 1);
                left++;    
            }

        }

        return totalSubstrings-count;
    }
}