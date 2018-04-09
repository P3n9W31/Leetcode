bool isPalindrome(int x) {
    int ans = 0;
    int num = x;
    if(x < 0)
        return 0;

    while(num > 0)
    {
        ans = ans * 10 + num % 10;
        num /= 10;
    }
    return ans == x;
}