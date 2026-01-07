return {
  {
    "tpope/vim-fugitive"
  },
  {
    "lewis6991/gitsigns.nvim",
    config = function()
     require('gitsigns').setup()

     -- Hunk operations
     vim.keymap.set("n", "<leader>gp", ":Gitsigns preview_hunk<CR>", {})
     vim.keymap.set("n", "<leader>gs", ":Gitsigns stage_hunk<CR>", {})
     vim.keymap.set("n", "<leader>gr", ":Gitsigns reset_hunk<CR>", {})
     vim.keymap.set("n", "<leader>gu", ":Gitsigns undo_stage_hunk<CR>", {})

     -- Git blame
     vim.keymap.set("n", "<leader>gb", ":Gitsigns toggle_current_line_blame<CR>", {})

     -- Navigate between hunks
     vim.keymap.set("n", "]c", ":Gitsigns next_hunk<CR>", {})
     vim.keymap.set("n", "[c", ":Gitsigns prev_hunk<CR>", {})
    end
  },
  {
    "rbong/vim-flog",
    dependencies = {
      "tpope/vim-fugitive",
    },
    config = function()
      -- Flog (visual git log)
      vim.keymap.set("n", "<leader>gl", ":Flog<CR>", {})
      vim.keymap.set("n", "<leader>gf", ":Flogsplit -path=%<CR>", {})
    end
  }
}
