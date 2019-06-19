class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False

        mlen = len(board)
        if mlen == 0:
            return False
        nlen = len(board[0])
        if nlen == 0:
            return False

        visited = set()
        for i in range(mlen):
            for j in range(nlen):
                visited.add((i, j))
                if board[i][j] == word[0] and search(board, i, j, word, 1, visited):
                    return True
                visited.remove((i, j))
        return False


def search(board, i, j, word, index, visited):
    if index == len(word):
        return True

    for adj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if adj[0] >= 0 and adj[0] < len(board) and adj[1] >= 0 and adj[1] < len(board[0]):
            if board[adj[0]][adj[1]] == word[index] and adj not in visited:
                visited.add(adj)
                if search(board, adj[0], adj[1], word, index + 1, visited):
                    return True
                visited.remove(adj)
