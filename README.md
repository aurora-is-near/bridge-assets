# Rainbow Bridge assets

This repository contains the metadata of Rainbow Bridge assets.

As `icon` field is required for NEP-141 tokens but is not presented in the official ERC-20 implementation,
this repository needs to contain all the information regarding the asset: name, symbol, decimals, icon.

Aurora team will ensure that all listed tokens contain the correct metadata.

## Adding a new asset
To add a new asset, please follow these steps:

1. First, you need to bridge your token using [Rainbow Bridge](https://ethereum.bridgetonear.org/). After this step you
   will have a NEAR NEP-141 token matching your ERC-20 token having the following address:
   `<YOUR_ERC_20_TOKEN_ADDRESS>.factory.bridge.near` (e.g. the USDT token will have the following address:
   `dac17f958d2ee523a2206206994597c13d831ec7.factory.bridge.near`.
2. Put an SVG icon to `tokens/` for your token with a name that matches the lower-case `symbol` of your ERC-20 token (e.g.
   `usdt.svg`).
3. Create a JSON file in `tokens/` with a name that matches the lower-case `symbol` of your ERC-20 token (e.g. `usdt.json`) and fill
   it with the following metadata (check the `tokens/example_token.json` file template):
   * `ethereum_address`: address of your ERC-20 token (with '0x' prefix) in Ethereum.
   * [OPTIONAL] `aurora_address`: address of your ERC-20 token (with '0x' prefix) in Aurora.
   * `name`: the human-readable name of the token. Must match the `name` of your ERC-20 token.
   * `symbol`: the abbreviation, like USDT or BTC. Must match the `symbol` of your ERC-20 token.
   * `decimals`: used in frontends to show the proper significant digits of a token. This concept is explained well in this [OpenZeppelin post](https://docs.openzeppelin.com/contracts/3.x/erc20#a-note-on-decimals).  Must match the `decimals` of your ERC-20 token.
   * [OPTIONAL] `icon`: a small image associated with this token. Must be a [data URL](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs), to help consumers display it quickly while protecting user data. Recommendation: use [optimized SVG](https://codepen.io/tigt/post/optimizing-svgs-in-data-uris), which can result in high-resolution images having small bytes size. Recommendation: create icons that will work well with both light-mode and dark-mode websites by either using middle-tone color schemes, or by [embedding media queries in the SVG](https://timkadlec.com/2013/04/media-queries-within-svg/). If you don't fill this field, we will use your `.svg` icon to fill this field by ourselves.
   * [OPTIONAL] `reference`: a link to a valid JSON file containing various keys offering supplementary details on the token. Example: "/ipfs/QmdmQXB2mzChmMeKY47C43LxUdg1NDJ5MWcKMKxDu7RgQm", "https://example.com/token.json", etc. If the information given in this document conflicts with the on-chain attributes, the values in reference shall be considered the source of truth. If you don't fill this field, please leave it empty and this field will be empty for your NEP-141 token.
   * [OPTIONAL] `reference_hash`: the base64-encoded sha256 hash of the JSON file contained in the reference field. This is to guard against off-chain tampering. If you don't fill this field, please leave it empty and this field will be empty for your NEP-141 token.
4. Fire a pull request having the following name: "Add <SYMBOL_OF_YOUR_ERC20_TOKEN> metadata" (e.g. "Add USDT metadata")
   having the previously mentioned files (JSON and SVG) in PR and having the content following the template:

   ```
   # Add USDT metadata

   ERC-20: https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7
   NEP-141: https://explorer.mainnet.near.org/accounts/dac17f958d2ee523a2206206994597c13d831ec7.factory.bridge.near
   ```
5. Aurora team will review your PR and update the metadata of your token.

## Adding a new asset (Testnet)
In case you want to add your Testnet token as well, please use the same procedure describe above, but use your `symbol` of ERC-20 and `_testnet` suffix within the file name. E.g.: `usdt_testnet.json`, `usdt_testnet.svg`.
