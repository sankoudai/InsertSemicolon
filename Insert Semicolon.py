import sublime_plugin
import sublime


class InsertSemicolonCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        commenter = "//"

        regions = self.view.sel()
        for region in regions:
            # In each selected region, put the last line to s
            line = self.view.line(region.b)
            s = self.view.substr(line)

            # Strip characters beyond commenter
            ind_commenter = s.find(commenter);
            if (ind_commenter > 0):
                s = s[0:t-1]

            ssize= len(s)
            # Line does not ends with space
            if not s.endswith(' '):
                self.view.insert(edit, line.b, ";")
                return

            # Line ends with space
            for i in range( ssize-1, 0, -1):
                if (s[i]==' ') and (s[i-1]!=' '):
                    index_close_space = i
                    self.view.insert(edit, line.a+index_close_space, ";")
                    return

        


