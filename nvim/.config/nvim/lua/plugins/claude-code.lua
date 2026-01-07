return {
  "greggh/claude-code.nvim",
  dependencies = {
    "nvim-lua/plenary.nvim",
  },
  config = function()
    require("claude-code").setup({
      split_ratio = 0.3,
      position = "botright vertical",
      enter_insert = true,
      use_git_root = true,
    })

    -- Custom keybindings
    vim.keymap.set('n', '<leader>cc', '<cmd>ClaudeCode<cr>', { desc = 'Toggle Claude Code' })
    vim.keymap.set('t', '<leader>cc', '<cmd>ClaudeCode<cr>', { desc = 'Toggle Claude Code' })
  end
}
