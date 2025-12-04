from django.core.management.base import BaseCommand
from core.models import Article


class Command(BaseCommand):
    help = 'Creates sample articles for testing'

    def handle(self, *args, **options):
        articles_data = [
            {
                'title': 'How to Start Investing as a Teenager',
                'slug': 'how-to-start-investing-as-a-teenager',
                'category': 'Investing',
                'description': 'A comprehensive guide for teenagers who want to begin their investment journey. Learn about basic investment concepts, setting up accounts, and making your first investment decisions.',
                'content': '''Starting to invest as a teenager can seem daunting, but it's one of the best decisions you can make for your financial future. Here's how to get started:

1. **Understand the Basics**
   - Learn about stocks, bonds, and mutual funds
   - Understand the concept of risk and return
   - Know the difference between saving and investing

2. **Start with Education**
   - Read books and articles about investing
   - Follow financial news
   - Take online courses on financial literacy

3. **Set Up an Account**
   - Many brokers offer custodial accounts for minors
   - You'll need a parent or guardian to help set this up
   - Research different broker options

4. **Start Small**
   - Begin with small amounts you can afford to lose
   - Focus on long-term investments rather than quick trades
   - Consider index funds for diversification

5. **Stay Consistent**
   - Invest regularly, even if it's a small amount
   - Reinvest dividends and returns
   - Review and adjust your strategy as you learn more

Remember, the key to successful investing is patience, education, and consistency. Start early, and let compound interest work in your favor!''',
                'for_students_only': True,
                'featured': True,
            },
            {
                'title': 'Basics of Budgeting for Students',
                'slug': 'basics-of-budgeting-for-students',
                'category': 'Personal Finance',
                'description': 'Learn how to create and stick to a budget as a student. Discover practical tips for managing your money, tracking expenses, and saving for your goals.',
                'content': '''Budgeting is a fundamental skill for financial success, especially for students who often have limited income. Here's how to create an effective budget:

**Step 1: Calculate Your Income**
- Include all sources: part-time jobs, allowances, scholarships
- Use your net income (after taxes) for accuracy
- Be realistic about irregular income

**Step 2: Track Your Expenses**
- Record everything you spend for at least a month
- Categorize expenses: food, transportation, entertainment, etc.
- Use apps or a simple spreadsheet

**Step 3: Create Categories**
- Essential expenses (rent, food, utilities)
- Education expenses (books, supplies)
- Savings (emergency fund, goals)
- Discretionary spending (entertainment, eating out)

**Step 4: Set Limits**
- Allocate specific amounts to each category
- Follow the 50/30/20 rule: 50% needs, 30% wants, 20% savings
- Adjust based on your situation

**Step 5: Monitor and Adjust**
- Review your budget weekly or monthly
- Adjust as your circumstances change
- Don't be too strict—allow for some flexibility

**Tips for Success:**
- Use budgeting apps like Mint or YNAB
- Set up automatic savings
- Find ways to cut unnecessary expenses
- Reward yourself for sticking to your budget

Remember, a budget isn't about restricting yourself—it's about making informed choices with your money!''',
                'for_students_only': True,
                'featured': False,
            },
            {
                'title': 'What Is Financial Literacy and Why Does It Matter?',
                'slug': 'what-is-financial-literacy-and-why-does-it-matter',
                'category': 'Financial Literacy',
                'description': 'An introduction to financial literacy: what it means, why it's important, and how it can impact your life. Essential reading for anyone starting their financial education journey.',
                'content': '''Financial literacy is the ability to understand and effectively use various financial skills, including personal financial management, budgeting, and investing. It's a crucial life skill that impacts every aspect of your financial well-being.

**What Financial Literacy Includes:**

1. **Basic Money Management**
   - Understanding income and expenses
   - Creating and maintaining a budget
   - Managing bank accounts and credit

2. **Saving and Investing**
   - Understanding different savings options
   - Basic investment principles
   - Retirement planning basics

3. **Debt Management**
   - Understanding different types of debt
   - Knowing how interest works
   - Strategies for paying off debt

4. **Risk Management**
   - Understanding insurance
   - Emergency fund planning
   - Protecting your financial future

**Why It Matters:**

- **Better Decision Making**: Financially literate people make better choices about money
- **Avoiding Debt Traps**: Understanding credit and debt prevents financial pitfalls
- **Building Wealth**: Knowledge leads to better investment and savings strategies
- **Financial Security**: Helps you build a secure financial future
- **Reduced Stress**: Money management skills reduce financial anxiety
- **Goal Achievement**: Helps you reach your financial goals faster

**How to Improve Your Financial Literacy:**

1. Read books and articles about personal finance
2. Take free online courses
3. Follow financial news and trends
4. Practice budgeting and tracking expenses
5. Join communities focused on financial education
6. Learn from experienced mentors

**Start Your Journey Today:**

Financial literacy is a journey, not a destination. Start with the basics and gradually build your knowledge. Every step you take toward financial literacy is an investment in your future.

At QazFinance, we're committed to helping young people develop these essential skills. Join our programs, read our articles, and start building your financial knowledge today!''',
                'for_students_only': False,
                'featured': True,
            },
        ]

        created_count = 0
        for article_data in articles_data:
            article, created = Article.objects.get_or_create(
                slug=article_data['slug'],
                defaults=article_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created article: {article.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Article already exists: {article.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully created {created_count} new article(s)')
        )

