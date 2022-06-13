# Rainbow Bridge assets

This repository contains the metadata of Rainbow Bridge assets.

As `icon` field is required for NEP-141 tokens but is not presented in the official ERC-20 implementation,
this repository needs to contain all the information regarding the asset: name, symbol, decimals, icon.

Aurora team will ensure that all listed tokens contain the correct metadata.

## Adding a new asset
To add a new asset, please follow these steps:

1. First, complete the deployment steps at [rainbowbridge.app/deploy](https://rainbowbridge.app/deploy).
   The app will inform the bridged token's deployment addresses and on-chain metadata.
   For example, NEP-141 tokens bridged from Ethereum ERC-20 have the format: `<YOUR_ERC_20_TOKEN_ADDRESS>.factory.bridge.near` (e.g. the USDT token will have the following address:
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
   * [OPTIONAL] `near_address`: if your token has a NEAR address (native NEAR or bridged via RainbowBridge), make sure to fill this field
   * [OPTIONAL] `icon`: a small image associated with this token. Must be a [data URL](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs), to help consumers display it quickly while protecting user data. Recommendation: use [optimized SVG](https://codepen.io/tigt/post/optimizing-svgs-in-data-uris), which can result in high-resolution images having small bytes size. Recommendation: create icons that will work well with both light-mode and dark-mode websites by either using middle-tone color schemes, or by [embedding media queries in the SVG](https://timkadlec.com/2013/04/media-queries-within-svg/). If you don't fill this field, we will use your `.svg` icon to fill this field by ourselves.
   * [OPTIONAL] `reference`: a link to a valid JSON file containing various keys offering supplementary details on the token. Example: "/ipfs/QmdmQXB2mzChmMeKY47C43LxUdg1NDJ5MWcKMKxDu7RgQm", "https://example.com/token.json", etc. If the information given in this document conflicts with the on-chain attributes, the values in reference shall be considered the source of truth. If you don't fill this field, please leave it empty and this field will be empty for your NEP-141 token.
   * [OPTIONAL] `reference_hash`: the base64-encoded sha256 hash of the JSON file contained in the reference field. This is to guard against off-chain tampering. If you don't fill this field, please leave it empty and this field will be empty for your NEP-141 token.
   * [OPTIONAL] `bridge": If your asset is being bridged not via Rainbow Bridge but using some other bridge, make sure to fill this field with the name of the used bridge (e.g. for the Allbridge tokens it will be "Allbridge")
4. Fire a pull request having the following name: "Add <SYMBOL_OF_YOUR_ERC20_TOKEN> token metadata" (e.g. "Add USDT token metadata")
   having the previously mentioned files (JSON and SVG) in PR and having the content following the template:

   ```
   # Add USDT token metadata

   ERC-20: https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7
   NEP-141: https://explorer.mainnet.near.org/accounts/dac17f958d2ee523a2206206994597c13d831ec7.factory.bridge.near
   Aurora ERC-20 (BlockScout): https://explorer.mainnet.aurora.dev/address/0x4988a896b1227218e4A686fdE5EabdcAbd91571f
   Aurora ERC-20 (Aurorascan): https://aurorascan.dev/address/0x4988a896b1227218e4A686fdE5EabdcAbd91571f
   ```
5. Aurora team will review your PR and update the metadata of your token. Always check the deployment status [here](https://rainbowbridge.app/deploy) (contract addresses, on-chain metadata, and storage registration when bridging to Aurora )
6. If your asset is being bridged not via Rainbow Bridge but using some other bridge, make sure to also add an abbreviation of the bridge to JSON and SVG files as a prefix. E.g. if you used Allbridge for USDT token, the file names should be `abr_usdt.json` and `abr_usdt.svg` respectively.

## Adding a new asset (Testnet)
In case you want to add your Testnet token as well, please use the same procedure describe above, but use your `symbol` of ERC-20 and `_testnet` suffix within the file name. E.g.: `usdt_testnet.json`, `usdt_testnet.svg`.
