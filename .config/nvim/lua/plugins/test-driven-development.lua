return {
	{
		"rgroli/other.nvim",
		config = function()
			require("other-nvim").setup({
				mappings = {
					"livewire",
					"angular",
					"laravel",
					"rails",
					"golang",
					"python",
					"react",
					"rust",
					{
            pattern = "/lib/(.*)/(.*).ex$",
            target = "/test/%1/%2_test.exs",
            context = "test",
          },
				},
				transformers = {
					lowercase = function(inputString)
						return inputString:lower()
					end,
				},
				style = {
					border = "solid",
					seperator = "|",
					width = 0.7,
					minHeight = 2,
				},
			})

      vim.api.nvim_set_keymap("n", "<leader>ll", "<cmd>:Other<CR>", { noremap = true, silent = true })
      vim.api.nvim_set_keymap("n", "<leader>ltn", "<cmd>:OtherTabNew<CR>", { noremap = true, silent = true })
      vim.api.nvim_set_keymap("n", "<leader>lp", "<cmd>:OtherSplit<CR>", { noremap = true, silent = true })
      vim.api.nvim_set_keymap("n", "<leader>lv", "<cmd>:OtherVSplit<CR>", { noremap = true, silent = true })
      vim.api.nvim_set_keymap("n", "<leader>lc", "<cmd>:OtherClear<CR>", { noremap = true, silent = true })

		end,
	},
}
