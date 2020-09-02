import string

dict = {}

texte = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis neque turpis, in gravida erat tincidunt a. Maecenas lobortis rutrum arcu, in posuere dolor fermentum sed. Duis imperdiet laoreet nibh, a pretium lectus condimentum eget. Maecenas eu elit vitae nibh euismod lacinia et a tortor. Donec at egestas leo, eget molestie quam. Sed elementum scelerisque sapien, quis suscipit ex malesuada vel. Aenean non mollis erat, in tincidunt massa.

Mauris semper, purus in dictum imperdiet, libero nunc bibendum ex, eget facilisis turpis lorem ac lorem. Sed bibendum scelerisque tortor vel dictum. Aliquam dignissim eget erat non mollis. Maecenas vehicula feugiat tortor, in vulputate ex molestie nec. Ut suscipit iaculis nulla, auctor elementum urna dapibus non. Fusce facilisis mollis tellus sit amet venenatis. Praesent metus enim, tincidunt posuere tellus et, placerat tincidunt justo.

Nunc id gravida ipsum, id porttitor magna. Maecenas porttitor accumsan odio non mattis. Suspendisse ultrices eleifend tristique. Vivamus accumsan libero tortor, eu aliquam sapien iaculis sed. In congue quis mi sed condimentum. Ut est libero, condimentum sit amet sagittis eu, tincidunt sed risus. Suspendisse pharetra molestie rutrum. Cras bibendum, dui ac consectetur eleifend, leo leo laoreet nibh, eget tristique lorem enim a nisi.

Duis a purus eu augue consectetur malesuada id nec ex. Pellentesque sed odio laoreet, imperdiet dui ut, sodales odio. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec interdum, tortor eu dapibus pharetra, libero nisi faucibus nisl, id malesuada felis diam id urna. Praesent est metus, gravida eu luctus vitae, egestas vel metus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras suscipit malesuada dui, vitae faucibus libero mollis a. In posuere blandit augue, sed semper ante imperdiet sed. Cras egestas posuere augue at semper. Praesent fermentum nunc risus, vitae aliquet augue consectetur a. Fusce interdum orci nunc, non posuere ex venenatis id. Nam faucibus fringilla mollis. Nulla ac enim accumsan, accumsan risus sit amet, rutrum tellus. Praesent lacinia augue at pulvinar venenatis. Etiam nunc augue, suscipit a faucibus sed, sodales ut mauris.

Quisque quis magna malesuada, ultricies leo eget, elementum est. Praesent enim purus, pretium a nisl quis, accumsan blandit sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris ultricies iaculis nunc, quis fringilla arcu bibendum ac. Integer eu sem eget dui tempor sagittis. Ut sit amet ipsum quis nisi porttitor pulvinar. Etiam suscipit, leo nec fringilla luctus, lacus est egestas augue, eget vestibulum augue diam non eros. Duis posuere ac magna eget ullamcorper.
"""

for letter in string.ascii_lowercase:
    dict[letter] = texte.count(letter)
print(dict)
