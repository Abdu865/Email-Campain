from pyhtml import *

t = html(
    head(),
    body(
    """Hello\n My name is Abdullah Hijazi with Universal Meditech Incorporated. \n\n
        We are a manufacturer of High Quality covid-19 antigen tests. Product infomration is attachment as SARS-COV-2 Antigen Rapid Test Colloidal Gold Kit.  Our tests are affordable, easy to use, and a positive result is granted in 2 minutes with 98% accuracy (detailed statistics in the attached product information).   Faster then PCR tests, our test is perfect for preventing an outbreak after a workplace exposure. \n \n 

        We are confident that our product will fulfill your organization’s needs. If you are interested in purchasing our tests, getting some free samples, or have any further inquiries, please contact me anytime.\n

        Thank you!\n\n
        Best regards,\n
        Abdullah Hijazi\n
        Sales Representative\n 
        Universal Meditech Inc. \n 
        1320 E. Fortune Ave #102. Fresno, CA 93725\n 
        Direct 304-751-5596 \n""",
        img(src="www.hijazz.solutions/gif")
    )
    ) 

email_contents = t.render()

