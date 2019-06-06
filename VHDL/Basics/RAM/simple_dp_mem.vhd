----------------------------------------------------------------------------------
-- Engineer: yoggi56
-- 
-- Create Date: 06.06.2019 20:58:25
-- Module Name: simple_dp_mem
-- Description: Simple Dual Port Memory
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity simple_dp_mem is
	Port ( clk : in STD_LOGIC;
		rst : in STD_LOGIC;

		data_in : in STD_LOGIC_VECTOR(15 downto 0);
		wr_adr  : in STD_LOGIC_VECTOR(9 downto 0);
		wr_en   : in STD_LOGIC;

		data_out : out STD_LOGIC_VECTOR(15 downto 0);
		rd_adr   : in  STD_LOGIC_VECTOR(9 downto 0)
	);
end simple_dp_mem;

architecture simple_dp_mem_arch of simple_dp_mem is

	-- 2D array type for the RAM
	type array_1kx16 is array(1023 downto 0) of std_logic_vector(15 downto 0);

	-- declare the RAM
	signal ram : array_1kx16;

begin

	process(clk)
	begin
		if rising_edge(clk) then
			if (wr_en = '1') then
				ram(to_integer(unsigned(wr_adr))) <= data_in;
				-- Read-during-write returns NEW data
				data_out <= ram(to_integer(unsigned(rd_adr)));
			else
				-- Read only
				data_out <= ram(to_integer(unsigned(rd_adr)));
			end if;
		end if;
	end process;
	
end simple_dp_mem_arch;
