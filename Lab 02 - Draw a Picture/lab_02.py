
import arcade


arcade.open_window(800, 600, "Drawing Example")

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

arcade.draw_rectangle_filled(680, 230, 50, 200, arcade.color.BLACK_BEAN)

arcade.draw_circle_filled(680, 300, 50, arcade.color.GREEN)
arcade.draw_circle_filled(630, 310, 50, arcade.color.GREEN)
arcade.draw_circle_filled(730, 310, 50, arcade.color.GREEN)
arcade.draw_circle_filled(680, 350, 50, arcade.color.GREEN)

arcade.draw_lrtb_rectangle_filled(30, 350, 400, 200, arcade.color.BISQUE)

arcade.draw_rectangle_filled(185, 244, 60, 90, arcade.color.BROWN)
arcade.draw_circle_filled(165, 245, 5, arcade.color.BLACK)

arcade.draw_triangle_filled(30, 400, 350, 400, 190, 500, arcade.color.BROWN)

arcade.draw_rectangle_outline(285, 340, 70, 70, arcade.color.BLACK)
arcade.draw_rectangle_outline(95, 340, 70, 70, arcade.color.BLACK)

arcade.draw_rectangle_filled(285, 340, 70, 70, arcade.color.AIR_FORCE_BLUE)
arcade.draw_rectangle_filled(95, 340, 70, 70, arcade.color.AIR_FORCE_BLUE)

arcade.draw_line(250, 340, 320, 340, arcade.color.BLACK, 3)
arcade.draw_line(285, 375, 285, 305, arcade.color.BLACK, 3)

arcade.draw_line(60, 340, 130, 340, arcade.color.BLACK, 3)
arcade.draw_line(95, 375, 95, 305, arcade.color.BLACK, 3)


arcade.finish_render()

arcade.run()