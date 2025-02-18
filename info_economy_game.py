"""
A Small Pygame Simulation of an Information-Theoretic Model of Economics.

Hypothesis/Idea: 
Using knowledge accumulation (reducing entropy) raises TFP, thereby raising wages 
and lowering time prices. The game loop illustrates this dynamic. 

"""

import pygame
import math
import random

# -----------------------------------------------------------------------------------
# GAME PARAMETERS
# -----------------------------------------------------------------------------------

# Number of possible production methods (finite Ω)
NUM_METHODS = 5

# Learning rate: how quickly research invests into "discovering" the best method
RESEARCH_RATE = 0.05

# The maximum entropy scenario is if p(ω) is uniform over NUM_METHODS
# For a uniform distribution, p(ω)=1/NUM_METHODS. Shannon Entropy = ln(NUM_METHODS).
H_max = math.log(NUM_METHODS)  # ln of 5 if NUM_METHODS=5

# Exponential TFP scaling factor α
ALPHA = 1.0

# Exponential time-price factor δ
DELTA = 0.7

# Production exponents
BETA = 0.5  # Let's assume a simple Y(t)=A(t)*(K^beta)*(L^(1-beta))
L_t = 10.0  # fixed labor for simplicity

# We'll define knowledge K(t) = H_max - H(p(ω;t)).
# We'll define TFP A(t) = exp(ALPHA * K(t)).
# We'll define the real wage w_r(t) ~ partial derivative wrt L of Y(t).
# We'll define time price ~ exp(-DELTA * K(t)).


# -----------------------------------------------------------------------------------
# HELPERS: ENTROPY, TFP, ETC.
# -----------------------------------------------------------------------------------
def shannon_entropy(prob_dist):
    """Compute Shannon entropy H(p) = -sum p(ω) ln p(ω)."""
    entropy = 0.0
    for p in prob_dist:
        if p > 0:
            entropy -= p * math.log(p)
    return entropy

def knowledge_stock(prob_dist):
    """K(t) = H_max - H(p)."""
    return H_max - shannon_entropy(prob_dist)

def tfp(prob_dist):
    """A(t) = exp(ALPHA * K(t))."""
    K = knowledge_stock(prob_dist)
    return math.exp(ALPHA * K)

def production(prob_dist, K_physical=10.0, L=10.0):
    """
    Y(t) = A(t)*K^BETA * L^(1-BETA).
    We'll assume we have some 'physical capital' K_physical.
    """
    A = tfp(prob_dist)
    return A * (K_physical**BETA) * (L**(1 - BETA))

def real_wage(prob_dist, K_physical=10.0, L=10.0):
    """
    w_r(t) = (1 - BETA) * exp(ALPHA*K) * K^BETA * L^BETA 
            (rough approximation from partial derivative).
    """
    K = knowledge_stock(prob_dist)
    A = math.exp(ALPHA * K)
    return (1 - BETA) * A * (K_physical**BETA) * (L**(BETA))

def time_price(prob_dist):
    """
    π_g(t) ∝ exp(-DELTA * K(t)).
    We simply define it as exactly exp(-DELTA*K(t)) for demonstration.
    """
    K = knowledge_stock(prob_dist)
    return math.exp(-DELTA * K)

# -----------------------------------------------------------------------------------
# RESEARCH MECHANICS
# -----------------------------------------------------------------------------------
def research(prob_dist):
    """
    Nudges p(ω) to concentrate around the 'true best method'.
    We'll define a hidden best method (the largest payoff).
    We can simulate that repeated research will shift p(ω) slightly 
    toward the best method index.
    """
    # We can define a single best method index (hidden) = 0...NUM_METHODS-1
    # Or random at the start of the game:
    # But for simplicity, let's keep it fixed at index 0.
    best_index = 0
    
    # SHIFT p(ω) toward best_index with some learning rate.
    # We'll do a naive approach: p(best_index) <- p(best_index)*(1+RESEARCH_RATE)
    # Then re-normalize.
    
    updated = prob_dist[:]
    updated[best_index] = updated[best_index] * (1.0 + RESEARCH_RATE)
    
    # Re-normalize
    s = sum(updated)
    updated = [p/s for p in updated]
    return updated

def produce_and_get_income(prob_dist, current_money):
    """
    Produces goods, returns updated 'money' or 'score'.
    Let the 'income' be proportional to production(prob_dist).
    """
    Y = production(prob_dist)
    income = Y * 1.0  # scale factor = 1.0
    new_money = current_money + income
    return new_money


# -----------------------------------------------------------------------------------
# GAME INITIALIZATION
# -----------------------------------------------------------------------------------
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Information-Theoretic Econ Game")

clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 18)
BIG_FONT = pygame.font.SysFont("Arial", 24)

# Probability distribution p(ω;t) starts uniform
prob_dist = [1.0 / NUM_METHODS for _ in range(NUM_METHODS)]

# Player resources
money = 0.0

# Colors
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
GRAY  = (180, 180, 180)
BLUE  = (100, 100, 255)
GREEN = (100, 255, 100)
RED   = (255, 100, 100)

# Button definitions
button_width = 150
button_height = 40

# Create "Invest in Research" button rect
research_button_rect = pygame.Rect(50, 500, button_width, button_height)
# Create "Invest in Production" button rect
produce_button_rect  = pygame.Rect(250, 500, button_width, button_height)

# Create "Quit" button
quit_button_rect     = pygame.Rect(650, 500, button_width, button_height)

# -----------------------------------------------------------------------------------
# MAIN GAME LOOP
# -----------------------------------------------------------------------------------
running = True
turn_count = 0

while running:
    clock.tick(30)  # limit to 30 FPS
    
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            # Check if clicked on "Research"
            if research_button_rect.collidepoint(mouse_pos):
                prob_dist = research(prob_dist)
                turn_count += 1
            
            # Check if clicked on "Produce"
            if produce_button_rect.collidepoint(mouse_pos):
                money = produce_and_get_income(prob_dist, money)
                turn_count += 1
            
            # Check if clicked on "Quit"
            if quit_button_rect.collidepoint(mouse_pos):
                running = False
    
    # DRAW BACKGROUND
    screen.fill(WHITE)
    
    # Compute Key Values
    H = shannon_entropy(prob_dist)
    K = knowledge_stock(prob_dist)
    A = tfp(prob_dist)
    wage = real_wage(prob_dist)
    tprice = time_price(prob_dist)
    Y = production(prob_dist)
    
    # RENDER TEXT
    title_surface = BIG_FONT.render("Info-Theoretic Economic Simulator", True, BLACK)
    screen.blit(title_surface, (50, 20))
    
    stats_lines = [
        f"Turn: {turn_count}",
        f"Entropy H(p): {H:.3f}",
        f"Knowledge K(t): {K:.3f}",
        f"TFP A(t): {A:.3f}",
        f"Real Wage w_r(t): {wage:.3f}",
        f"Time Price π_g(t): {tprice:.3f}",
        f"Production Y(t): {Y:.3f}",
        f"Money (score): {money:.2f}",
    ]
    
    for i, line in enumerate(stats_lines):
        txt_surf = FONT.render(line, True, BLACK)
        screen.blit(txt_surf, (50, 60 + 20*i))
    
    # DRAW PROB DISTRIBUTION BARS
    bar_x = 50
    bar_y = 250
    bar_height = 20
    bar_gap = 10
    
    dist_title = FONT.render("Probability Distribution p(ω):", True, BLACK)
    screen.blit(dist_title, (50, 220))
    
    for i, p in enumerate(prob_dist):
        # length of bar in pixels (scale up by some factor, e.g. 300)
        length = int(300 * p)
        bar_rect = pygame.Rect(bar_x, bar_y + i*(bar_height+bar_gap), length, bar_height)
        pygame.draw.rect(screen, BLUE, bar_rect)
        
        # label each bar
        bar_label = FONT.render(f"Method {i}: {p:.3f}", True, BLACK)
        screen.blit(bar_label, (bar_x + length + 5, bar_y + i*(bar_height+bar_gap)))
    
    # DRAW BUTTONS
    pygame.draw.rect(screen, GREEN, research_button_rect)
    pygame.draw.rect(screen, BLUE, produce_button_rect)
    pygame.draw.rect(screen, RED, quit_button_rect)
    
    # Button labels
    research_label = FONT.render("Research", True, BLACK)
    screen.blit(research_label, (research_button_rect.x + 10, research_button_rect.y + 10))
    
    produce_label = FONT.render("Produce", True, BLACK)
    screen.blit(produce_label, (produce_button_rect.x + 10, produce_button_rect.y + 10))
    
    quit_label = FONT.render("Quit", True, BLACK)
    screen.blit(quit_label, (quit_button_rect.x + 30, quit_button_rect.y + 10))
    
    # UPDATE DISPLAY
    pygame.display.flip()

pygame.quit()
