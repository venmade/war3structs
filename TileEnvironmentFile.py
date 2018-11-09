from construct import *
from structs.common import *

"""
  Formats: w3e

  The tile environment file contains the map's tile and cliff data.
"""

TileEnvironmentHeader = Struct(
  "file_id" / Const(b"W3E!"),
  "version" / Integer,
  "tileset_id" / TilesetEnum,
  "custom_tilesets" / Integer,
  "ground_tileset_ids_count" / Integer,
  "ground_tileset_ids" / Array(this.ground_tileset_ids_count, ByteId),
  "cliff_tileset_ids_count" / Integer,
  "cliff_tileset_ids" / Array(this.cliff_tileset_ids_count, ByteId),
  "map_width" / Integer,
  "map_height" / Integer,
  "map_center_offset_x" / Float,
  "map_center_offset_y" / Float
)

TilePoint = Bitwise(Struct(
  "ground_height" / Bytewise(Short),
  "water_level" / Bytewise(Short),
  "flags" / FlagsEnum(Nibble,
    boundary_flag_first  = 0x4000,
    ramps                = 0x0010,
    use_blight_default   = 0x0020,
    water_enabled        = 0x0040,
    boundary_flag_second = 0x0080
  ),
  "ground_texture_type" / Nibble,
  "texture_details" / Octet,
  "cliff_texture_type" / Nibble,
  "layer_height" / Nibble
))

TileEnvironmentFile = Struct(
  "header" / TileEnvironmentHeader,
  "data" / Array(this.header.map_width * this.header.map_height, TilePoint)
)
