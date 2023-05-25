from ebooklib import epub
from ..sites import switch as switch


#https://stackoverflow.com/questions/64383172/how-to-create-a-link-which-points-to-the-a-potion-of-a-chapter-by-using-ebooklib to handle append to toc
#do an ifinite loop to add chapter and toc location with an exit condition given by the site file

def makebook(url):
    book = epub.EpubBook()
    # set metadata
    book.set_identifier("id123456")
    book.set_title(switch.gettitle)
    book.set_language("en")
    book.add_author(switch.getauthor(url))
    chapter_list = switch.getchapterlist(url)
    index = 0
    for chapter in chapter_list:
        c1 = epub.EpubHtml(title=switch.gettitle(chapter), file_name=f"chap_{index}.xhtml", lang="en")
        c1.content = (str(switch.getbody(chapter)))
        book.add_item(c1)
        index = index + 1

    # define Table Of Contents
    book.toc = (
        epub.Link("chap_01.xhtml", "Introduction", "intro"),
        (epub.Section("Simple book"), (c1,)),
    )

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

    # basic spine
    book.spine = ["nav", c1]

    # write to the file
    epub.write_epub("test.epub", book, {})



