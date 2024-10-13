import feedparser
import os

RSS_LIST = "./rss_list"
DEBUG=False
 
# CONTEXTE :
# Un FEED (aussi nommé flux RSS ou 'd') est une liste d'ENTRIES (aussi nommée "items")
# Chaque objet FEED ('d') contient une description (d.feed) et une liste d'entries (d.entries)

def print_entry(entry):
     # print le titre d'une entry
     if 'title' in entry:
        print(entry.title)

def print_feed_entries(d):
    # print les entries d'un feed
    if 'entries' in d:
        for i in d.entries:
            print_entry(i)
        return False
    else:
        return ValueError

def print_feed_info(d):
    # print la description d'un feed
    if 'title' in d.feed:
        print("Titre : " + d.feed.title)
    if 'link' in d.feed:
        print("Lien : " + d.feed.link)
    if 'description' in d.feed:
        print("Description : " + d.feed.description)
    if 'published' in d.feed:
        print("Publié : " + d.feed.published)
    if 'published_parsed' in d.feed:
        print("Parsé : " + d.feed.published_parsed)

def print_feed(d):
    # print un feed
    print("=====NEW FEED===")
    print_feed_info(i)
    print("=====ENTRIES====")
    print_feed_entries(d)
    print("================")

def read_rss_list_file():
    # lis un fichier de liens rss (typiquement ./rss_list) et renvoie une liste d'objets feed
    feed_list = []
    if os.path.exists(RSS_LIST):
            with open(RSS_LIST, 'r') as file:
                for i in file:
                    if DEBUG:
                        print ("Processing : " + i, end='')
                    d = feedparser.parse(i)
                    if 'title' in d.feed:
                        feed_list.append(d)
    if DEBUG:
        print('')
    return feed_list

def check_entry(entry):
    # Renvoie True si une liste correspond à un critère quelconque (par exemple titre exact à une valeur donnée)
    if (entry.title == "Pirate IPTV Reseller Who Made Millions of Euros Sent to Prison For Eight Years"):
        #print(entry.summary)
        #print(entry.summary_detail)
        print(entry.description)
        return True
    return False


def match(entries_list):
    # applique une fonction check_XXX() sur tous les éléments d'une liste d'entries.
    # renvoie, séparément, les matchs et les non-matchs.
    x,y, match_entries, non_match_entries = 0, 0, [], []
    for i in entries_list:
        x += 1
        if DEBUG:
            print (i.title)
        if (check_entry(i)):
            y += 1
            match_entries.append(i)
        else:
            non_match_entries.append(i)
    if DEBUG:
        print(f"match() : {y} items matched out of {x}.")
    return match_entries, non_match_entries

if __name__ == '__main__':
    feed_list = read_rss_list_file() # On crée une liste de tous les feeds

    entries_list=[] # On reformate cette liste de feeds en une seule grande liste d'items
    for i in feed_list:
        if 'entries' in i:
            for j in i.entries:
                entries_list.append(j)
    
    #print(entries_list)
    match(entries_list) # On teste un par un les élements de la liste
