import {Dex} from '@pkmn/dex';
import {Sets} from '@pkmn/sets';

const set = Sets.unpack(
  'Tangrowth||assaultvest|H|gigadrain,knockoff,powerwhip' +
  ',earthquake|Sassy|248,,8,,252,||,30,30,,,|||,ice,',
  Dex.forGen(6)
);

console.log(set)