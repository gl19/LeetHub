class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        final_path = []
        for folder in path_list:
            if folder in ('/', '.', ''):
                continue
            elif folder == '..':
                if len(final_path) > 0:
                    final_path.pop()
            else:
                final_path.append(folder)
        
        return '/' + '/'.join(final_path)

            

            