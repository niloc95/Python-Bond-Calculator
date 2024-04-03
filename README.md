# A Python Bond Calculator

* Python
* @author: Nilo Cara 
* @copyright:   Copyright (c) 2023, Nilo Cara
* @link:   https://niloc95.github.io/niloc95
* @since:  v1.0
* Website: https://frontend.co.za
* Twitter: [@CodeCara](https://twitter.com/CodeCara)
* GitHub: [@niloc95](https://github.com/niloc95)
* LinkedIn: [@https:\/\/www.linkedin.com\/in\/nilo-cara\/](https://linkedin.com/in/https:\/\/www.linkedin.com\/in\/nilo-cara\/)
* Date: October 2023

## Description 

This Project involves developing a program to calculate interest on an investment or determine the monthly repayment amount for a home loan. Before diving into the development, users will gain a basic understanding of interest, a fundamental concept in finance. Interest manifests in various financial transactions, such as loans and investments, impacting the overall amount one either pays or earns. There are two primary types of interest: simple and compound.

Simple Interest: Calculated based on the initial investment amount (principal) and applied once per year. The interest earned is added to the principal amount for subsequent calculations. For instance, investing R1000 at 10% interest would yield R100 interest in the first year, resulting in a total of R1100. In subsequent years, the interest continues to be calculated on the initial principal amount.

Compound Interest: Contrastingly, compound interest involves calculating interest on the current total, known as the accumulated amount. Continuing with the R1000 investment at 10% compounded annually, the first year would yield R100 interest, resulting in an accumulated amount of R1100. However, in the second year, interest is calculated on the new total (R1100), leading to a higher interest amount and consequently a higher accumulated amount (R1210).

Understanding these concepts is crucial for developing a robust program capable of accurately calculating interest and repayment amounts for various financial scenarios.

## To implement in production: 

It handles both GET and POST requests. When a POST request is received, it processes the form data, performs the calculations, and renders the appropriate result template (result.html). If the request method is GET, it renders the form template (form.html). Additionally, if the user selects neither "Investment" nor "Bond", an error template (error.html) is rendered.

You need to create templates for form.html, result.html, and error.html, and also configure your urls.py accordingly.

