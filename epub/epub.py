from ebooklib import epub

#https://stackoverflow.com/questions/64383172/how-to-create-a-link-which-points-to-the-a-potion-of-a-chapter-by-using-ebooklib to handle append to toc
#do an ifinite loop to add chapter and toc location with an exit condition given by the site file
book = epub.EpubBook()

# set metadata
book.set_identifier("id123456")
book.set_title("Sample book")
book.set_language("en")

book.add_author("Author Authorowski")
book.add_author(
    "Danko Bananko",
    file_as="Gospodin Danko Bananko",
    role="ill",
    uid="coauthor",
)


url_list = [] #in implementation call a get url's method that will go to the switch and give either 1 page or a chapter list


# this works now, do the list of url method.
#c1 = epub.EpubHtml(title="Intro", file_name="chap_01.xhtml", lang="hr")

#c1.content = (str(m_body("https://www.marxists.org/archive/bookchin/1969/listen-marxist.htm")))



# add chapter
book.add_item(c1)
# add image


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