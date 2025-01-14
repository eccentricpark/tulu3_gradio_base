# CSS를 지정합니다.
def get_css():
    custom_css = """ 
    #custom_input textarea .prose * {
        font-size: 16px;
    }
    #custom_output .prose * {
        font-size: 16px;
    }
    .cm-line {
        font-size: 18px !important;
    }
    """
    return custom_css