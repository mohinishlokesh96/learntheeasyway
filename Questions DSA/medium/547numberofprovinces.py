# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city
# b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1
# if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.
class Solution:
    #Approach1:(Depth First Search)
    #Time Compelxity:O(n^2)
    #Space Compelxity:O(n)
    def findCircleNum(self,isConnected):
        rows=len(isConnected)
        cols=len(isConnected[0])
        node_dict={i: [] for i in range(rows)}
        for i in range(rows):
            for j in range(cols):
                if i != j and isConnected[i][j] == 1:
                    node_dict[i].append(j)
        provinces=0
        visited=set()
        def dfs(node, node_dict, visited):
            if node in visited:
                return
            else:
                visited.add(node)
                for nodes in node_dict[node]:
                    dfs(nodes, node_dict, visited)
        for i in node_dict.keys():
            if i not in visited:
                dfs(i, node_dict, visited)
                provinces+=1
        return provinces

sol = Solution()
print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
