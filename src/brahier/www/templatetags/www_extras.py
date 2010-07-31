from django import template
from brahier.navigation import NAVIGATION

ALWAYS_OPEN = 0

register = template.Library()

@register.simple_tag
def navigation(request, active_node_id):
    
    def tree_of(navigation):
        """ converts the simple navigation array to a tree """

        result = []
        for i in navigation:
            node = {
                'id' : i[0], 'text'  : i[1],
                'url': i[2], 'option': i[3]
            }
            if len(i) >= 5:
                node['children'] = tree_of(i[4])
            else:
                node['children'] = None
            result.append(node)
        return result   
    
    def tag(tree, level):
        """ add the level, selected and open attributes of the tree """
        
        res = False
        for node in tree:
            node['level'] = level
            if active_node_id != '' and node['id'] == active_node_id:
                node['selected'] = True
            else:
                node['selected'] = False
                    
            if node['children'] is not None:
                node['open'] = tag(node['children'], level + 1)
            else:
                node['open'] = False
            
            res = res or node['selected'] or node['open']


        return res
        
    def render(tree, level):
        """ render the tree in HTML. this is site specific """

        indent = " " * level*2
        res = "<ul class=\"nav_tree nav_level_%i\">\n" % level
        for node in tree:
            classes = ["nav_node", "nav_level_%s" % level]
            if node['selected']:
                classes.append("nav_selected")
            if node['open']:
                classes.append("nav_open")
            res += indent + "  " + "<li id=\"%s\" class=\"%s\">" % \
                ("nav_" + node['id'], " ".join(classes))
            if node['url'] is None or node['selected']:
                res += node['text']
            else:
                res += "<a href=\"%s\">%s</a>" % (node['url'], node['text'])
            if node['children'] is not None \
                and (node['selected'] or node['open'] \
                     or node['level'] < ALWAYS_OPEN):
                res += render(node['children'], level+1)
            res += "</li>\n"
        res += indent + "</ul>\n"
        return res
    
    tree = tree_of(NAVIGATION)
    tag(tree, 0)
    return render(tree,0)
