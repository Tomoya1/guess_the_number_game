def markdownHtmlConverter(mdfile, htmlfile):
    contents = "";
    htmlcontents = "";

    # open mdfile
    with open(mdfile) as f:
        contents = f.read();
    
    # convert
    import markdown
    htmlcontents = markdown.markdown(contents);

    # write htmlfile
    with open(htmlfile, 'w') as f:
        f.write(htmlcontents);



# process separately
import sys
args = sys.argv

if args[1] == "markdown":
    markdownHtmlConverter(args[2], args[3]);