
class Solution {
    // Function to check whether the number evenly divides n.
    evenlyDivides(n) {
        let count = 0;
        let originalNumber = n; // Store the original number for later use

        while (n > 0) {
            let lastDigit = n % 10; // Extract the last digit

            // Check if the last digit divides the original number
            if (lastDigit !== 0 && originalNumber % lastDigit  === 0) {
                count += 1;
            }

            n = Math.floor(n / 10); // Remove the last digit
        }

        return count;
    }
}