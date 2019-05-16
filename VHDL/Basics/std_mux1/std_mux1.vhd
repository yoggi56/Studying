----------------------------------------------------------------------------------
-- Module Name: std_mux1
-- Description: Standard two-input bus multiplexer which is realized using 
--              standard logic gates
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity std_mux1 is
    Port ( in_1 : in STD_LOGIC_VECTOR (3 downto 0);
           in_2 : in STD_LOGIC_VECTOR (3 downto 0);
           in_3 : in STD_LOGIC;
           out_1 : out STD_LOGIC_VECTOR (3 downto 0)
		);
end std_mux1;

architecture std_nux1_arch of std_mux1 is

	signal in_3_bus : std_logic_vector(3 downto 0);

begin
	--------------------------------------------------------------------
	-- FIRST approach
	-- in_3_bus <= (in_3 & in_3 & in_3 & in_3);
	
	-- out_1 <= ((NOT in_3_bus) AND in_1) OR (in_3_bus AND in_2);
	--------------------------------------------------------------------
	-- SECOND approach
	-- with (in_3) select
		-- out_1 <= 	in_1 when '0',
					-- in_2 when '1',
					-- "0000" when others;
	--------------------------------------------------------------------			
	-- THIRD approach
	out_1 <= 	in_1 when in_3 <= '0' else
				in_2 when in_3 <= '1' else "0000";
	--------------------------------------------------------------------

end std_nux1_arch;
