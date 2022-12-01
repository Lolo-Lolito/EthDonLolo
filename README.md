# Concept

In the last time, we have experienced some difficulties to get some ETH on testnets. Therefore, for builders, it can be difficult to get the fuel to test their contracts. This application aims to help the builder to find this precious ETHs.

It is a donation platform. The builders can register to inform that they need some ETHs. They can give their names, their github, the reasons and the amount they need.
People who want to donate can then choice to who they want to donate based on this information. They can also to donate to all.

# Requirement

## Vocabular

Requester : the person who requests the donation
Donor : the person who donates

## Requester

Requester send his request to the smart contract, he can provide the following information :
-his name,
-his github,
-the reason why he needs the donation,
-the amount of ETH he needs.
*-> Okay, has been implemented and unit tested*

These information are public.
*-> Okay, has been implemented*

He can only submit one request.
*-> Okay, has been implemented and unit tested*

He can modify his request.
*-> Okay, has been implemented and unit tested*

He can remove his request.
*-> Okay, has been implemented and unit tested*

The amount of ETH he needs is updated according to the amount send by the donor.
*-> Okay, has been implemented and unit tested*

When the amount of ETH requested has been covered by the donation, the request is removed from the smart contract.
*-> Okay, has been implemented and unit tested*

## Donor

Donor has access to the list of requests.
*-> Okay, has been implemented and unit tested*

He can read the information of all of the requests.
*-> Okay, has been implemented and unit tested*

He can choose to donate the amount of ETH he wants.
*-> Okay, has been implemented and unit tested*

He can donate to the requester he choose to help.
*-> Okay, has been implemented and unit tested*

He can donate to all the requester. In this case, the amount of ETH, he give will be splitted between all the requester.
*-> Okay, has been implemented and unit tested*




