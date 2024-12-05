from lxml.html import fromstring


class LinkedinScraper:

    def __init__(self, response_text, url) -> None:
        self.parser = fromstring(response_text)
        self.url = url

    def validate_structure(self):
        if self.parser.xpath("//div[contains(@class, 'article-main__content')]//h3"):
            return "content_type_1"
        if self.parser.xpath("//div[contains(@class, 'article-main__content')]//strong"):
            return "content_type_2"
        else:
            return "general_content"


    def extract_pulse_title_and_author(self):
        
        data = {}

        #Fetch Title
        title = self.parser.xpath("//h1/text()")
        data["title"] = title[0]

        #Fetch Author Details
        author_name = self.parser.xpath("//h3[contains(@class, 'base-main-card__title')]/text()")[0].strip()
        data["author"] = author_name

        linkedin_url = self.parser.xpath("//a[contains(@class, 'base-card__full-link')]/@href")[0].strip()
        data["linkedin_url"] = linkedin_url
        
        bio = self.parser.xpath("//h4[contains(@class, 'base-main-card__subtitle')]/text()")[0].strip()
        data["bio"] = bio

        return data


    def extract_pulse_type1_content(self):
        div = self.parser.xpath("//div[contains(@class, 'article-main__content')]")[0]
        headings = div.xpath(".//h3 | .//strong") 

        result = []
        for _, heading in enumerate(headings):
        
            heading_text = heading.text_content().strip()
            content = []
            sibling = heading.getnext()

            while sibling is not None and sibling.tag not in ['h3', 'strong']:
                content.append(sibling.text_content().strip())
                sibling = sibling.getnext()
            
            result.append({
                "heading": heading_text,
                "content": " ".join(content)
            })

        return result


    def extract_data(self):
        json_data = {}

        category = "unknown"

        if "linkedin.com/blog" in self.url:
            category = "blog"
        elif "linkedin.com/pulse/" in self.url:
            category = "pulse"
        elif "linkedin.com/posts" in self.url:
            category = "posts"
        elif "linkedin.com/business/marketing/blog/" in self.url:
            category = "business"

        if category == "pulse":
            content_type = self.validate_structure()

            if content_type == "content_type_1":
                json_data = self.extract_pulse_title_and_author()
                json_data["blog_content"] = self.extract_pulse_type1_content()
            
            elif content_type == "content_type_2":
                pass
    
        


        return json_data