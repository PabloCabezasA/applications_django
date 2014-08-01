from django.forms import ModelForm
from myweb.models import AccountAccount

# Create the form class.
class AccountAccountForm(ModelForm):
     class Meta:
         model = AccountAccount
         #fields = ['pub_date', 'headline', 'content', 'reporter']

# Creating a form to add an article.
#form = ArticleForm()
# Creating a form to change an existing article.
#article = Article.objects.get(pk=1)
#form = ArticleForm(instance=article)