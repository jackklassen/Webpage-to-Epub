from ebooklib import epub
import switch as switch


#https://stackoverflow.com/questions/64383172/how-to-create-a-link-which-points-to-the-a-potion-of-a-chapter-by-using-ebooklib to handle append to toc
#do an ifinite loop to add chapter and toc location with an exit condition given by the site file

def makebook(url,location):
    book = epub.EpubBook()
    # set metadata
    book.set_identifier("id123456")
    book.set_title(switch.gettitle(url))
    book.set_language("en")
    book.add_author(switch.getauthor(url))
    chapter_list = switch.getchapterlist(url)
    index = 0
    
    toc = list()
    book.spine = ["nav"]
    
    for chapter in chapter_list:
        title = switch.getchaptertitle(chapter)
        filename = f"chap_{index}.xhtml"
        
        print(f"title: {title} filename: {filename}")
        
        c1 = epub.EpubHtml(title=title, file_name=filename, lang="en")
        c1.content = ('<html><body><p>' + str(switch.getbody(chapter)) + '</p></body></html>')
        
        book.add_item(c1)
        link = epub.Link(filename,title,index)
        #toc.append(link)
        book.spine.append(c1)
        
        index = index + 1

    #toc = tuple(toc)
    #book.toc = toc #as of right now this only causes errors

    # add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # define CSS style
    style = "BODY {color: white;}"
    nav_css = epub.EpubItem(
        uid="style_nav",
        file_name="style/nav.css",
        media_type="text/css",
        content=style,
    )

    # add CSS file
    book.add_item(nav_css)

    if(location == ''):
         # write to the file
        output_file_name_raw = (switch.gettitle(url) + '.epub')
        epub.write_epub(output_file_name_raw, book, {})
    
    else:
        # write to the file
        output_file_name_raw = (location + "/" + switch.gettitle(url) + '.epub')
        epub.write_epub(output_file_name_raw, book, {})





