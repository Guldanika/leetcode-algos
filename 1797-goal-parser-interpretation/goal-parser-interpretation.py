class Solution:
    def interpret(self, command: str) -> str:
        ans = (command
        .replace('()', 'o')
        .replace('(al)', 'al'))
        return ans