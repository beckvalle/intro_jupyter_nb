
def hl_feats():
    import os
    import ipywidgets as widgets
    from IPython.display import display, clear_output
    from ipywidgets.widgets.interaction import show_inline_matplotlib_plots
    
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    from matplotlib.patches import Rectangle
    from matplotlib.collections import PatchCollection
    

    def show_image(rb_inst):
        with out:
            clear_output()
            
            if select_img.value == 'Notebook Dashboard':
                if select_feat.value == 'Select an item':
                    w_img=mpimg.imread(os.path.join('img', 'Jupyter_select.png'))
                else:
                    w_img=mpimg.imread(os.path.join('img', 'Jupyter_dashboard.png'))
                    
            if select_img.value == 'Notebook':
                if select_feat.value == 'Command palette':
                    w_img=mpimg.imread(os.path.join('img', 'tool_bar_shortcut.png'))
                else:
                    w_img=mpimg.imread(os.path.join('img', 'Jupyter_notebook_head.png'))
                
            if select_img.value == 'Notebook Cells': 
                w_img=mpimg.imread(os.path.join('img', 'Jupyter_cells.png')) 
                
            if select_img.value == 'Select':
                feat_desc.value = ''
                return

            plt.figure(figsize = (20,5))
            plt.imshow(w_img)
            plt.axis('off')
            
            rect_patch = None
             
            if select_feat.value == "'Files' tab":
                rect_patch = plt.Rectangle((0, 32), 40, 60, fill=None, edgecolor='r', linewidth=2)
                feat_desc.value = '<b>Feature Description</b>: This tab displays a window where you can view your files.'
            if select_feat.value == "Files list":
                rect_patch = plt.Rectangle((40, 170), 400, 120, fill=None, edgecolor='r', linewidth=2)
                feat_desc.value = '<b>Feature Description</b>: All of your notebooks, files, and folders are displayed here.'
            if select_feat.value == 'Select an item':
                rect_patch = plt.Rectangle((100, 140), 400, 375, fill=None, edgecolor='r', linewidth=2)
                feat_desc.value = '<b>Feature Description</b>: After right clicking an item, you can view a menu that shows the actions you can take with it - these actions will change depending on what you have selected (notebook, file, or folder) and if the notebook is currently running. Actions include duplicating, renaming, moving, downloading, viewing, editing, or deleting an item, or shutting down a notebook.'
                
                
            if select_feat.value == "'New' button":    
                rect_patch = plt.Rectangle((50, 40), 100, 30, fill=None, edgecolor='r', linewidth=2)
                feat_desc.value = '<b>Feature Description</b>: You can create a new notebook, text file, or folder using this button.'
            if select_feat.value == 'Notebook title':
                rect_patch = plt.Rectangle((360, 50), 280, 35, fill=None, edgecolor='r', linewidth=2)
                feat_desc.value = '<b>Feature Description</b>: The notebook title is displayed here.'
            if select_feat.value == 'Save status':
                rect_patch = plt.Rectangle((250, 520), 110, 30, fill=None, edgecolor='r', linewidth=2)
                feat_desc.value = '<b>Feature Description</b>: This indicates when the notebook was last saved. Save often!'
            if select_feat.value == 'Menu bar':
                rect_patch = plt.Rectangle((40, 5), 500, 35, fill=None, edgecolor='r', linewidth=2)
                feat_desc.value = '<b>Feature Description</b>: Various actions can be taken from the menu bar. A common action is restarting the kernel.'
            if select_feat.value == 'Tool bar':
                rect_patch = plt.Rectangle((360, 80), 610, 35, fill=None, edgecolor='r', linewidth=2)
                feat_desc.value = '<b>Feature Description</b>: Shortcuts for common actions are located here. Save using the left-most button often!'
            if select_feat.value == 'Cell type selector':
                rect_patch = plt.Rectangle((710, 80), 120, 35, fill=None, edgecolor='r', linewidth=2)
                feat_desc.value = "<b>Feature Description</b>: You can use this dropdown to change the type of your selected cell(s). The two most common cell types are 'Code' and 'Markdown'."
            if select_feat.value == 'Command palette': 
                rect_patch = plt.Rectangle((150, 40), 400, 35, fill=None, edgecolor='r', linewidth=2)
                feat_desc.value = '<b>Feature Description</b>: Open View->Activate Command Palette or press Ctrl+Shift+C to open the command palette. Clicking here will bring up a useful list of keyboard shortcuts.'

                
            if select_feat.value == 'Markdown cell':
                rect_patch = plt.Rectangle((50, 24), 1000, 120, fill=None, edgecolor='r', linewidth=2)
                feat_desc.value = '<b>Feature Description</b>: This is a markdown cell. Use it for descriptive text and headings. Both HTML and Jupyter Markdown formatting can be used to style text.'
            if select_feat.value == 'Code cell':
                rect_patch = plt.Rectangle((50, 150), 1500, 90, fill=None, edgecolor='r', linewidth=2)
                feat_desc.value = '<b>Feature Description</b>: This is a code cell. You can run script snippets here.'
            if select_feat.value == 'Cell status':
                rect_patch = plt.Rectangle((0, 150), 50, 30, fill=None, edgecolor='r', linewidth=2)
                feat_desc.value = "<b>Feature Description</b>: This number tells you the order that the cells have been run in. If it is blank, the cell hasn't been run. If it has an *, the cell is currently running."

            if rect_patch:
                plt.gca().add_patch(rect_patch)

            show_inline_matplotlib_plots()
            
    def show_opts(dd_inst):
        if dd_inst.new == 'Notebook Dashboard':
            select_feat.options = ["'Files' tab", 'Files list', 'Select an item', "'New' button"]
        if dd_inst.new == 'Notebook':
            select_feat.options = ['Notebook title', 'Save status', 'Menu bar', 'Tool bar', 'Cell type selector', 'Command palette']
        if dd_inst.new == 'Notebook Cells':
            select_feat.options = ['Markdown cell', 'Code cell', 'Cell status']
        if dd_inst.new == 'Select':
            select_feat.options = []
        
    
    global select_img
    global select_feat
    global feat_desc
    select_img = widgets.Dropdown(options=['Select', 'Notebook Dashboard', 'Notebook', 'Notebook Cells'], description='Section:')
    select_feat = widgets.RadioButtons(options=[], description='Features:')
    feat_desc = widgets.HTML(value='')
        
    out = widgets.Output()
        
    select_img.observe(show_opts, names='value')
    select_feat.observe(show_image, names='value')
    
    display(select_img)
    display(select_feat)
    display(feat_desc)
    display(out)
    
    
    