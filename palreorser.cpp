#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// Function to find the longest palindromic substring in the given string
string findLongestPalindrome(const string &input) {
    int length = input.length();
    if (length == 0) return "none";

    string maxPalindrome = "none";
    
    for (int start = 0; start < length; ++start) {
        for (int end = start + 1; end <= length; ++end) {
            string sub = input.substr(start, end - start);
            string revSub = sub;
            reverse(revSub.begin(), revSub.end());
            
            if (sub == revSub && sub.length() > maxPalindrome.length() && sub.length() > 2) {
                maxPalindrome = sub;
            }
        }
    }
    return maxPalindrome;
}

// Function to transform the output by concatenating the token and replacing every third character with 'X'
string modifyOutput(const string &palindrome, const string &token) {
    string combined = palindrome + token;
    for (int index = 2; index < combined.length(); index += 3) {
        combined[index] = 'X';
    }
    return combined;
}

// Main challenge function
string SearchingChallenge(string str) {
    // Find the longest palindromic substring
    string palindrome = findLongestPalindrome(str);
    
    // Challenge token
    string challengeToken = "w391ncgd7e";
    
    // Transform the output
    string finalResult = modifyOutput(palindrome, challengeToken);
    
    return finalResult;
}

int main(void) {
    // Keep this function call here
    cout << SearchingChallenge("hellosannasmith") << endl;  // Example input
    return 0;
}
